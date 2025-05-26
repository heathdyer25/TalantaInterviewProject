const selectAllBtn = document.getElementById('selectAllBtn');
const deselectAllBtn = document.getElementById('deselectAllBtn');
const checkboxes = document.querySelectorAll('input[type="checkbox"]');
const fetchBtn = document.getElementById('fetchBtn');

// when select all is pressed 
selectAllBtn.addEventListener('click', () => {
    checkboxes.forEach(cb => cb.checked = true);
});

// when deselect all is pressed
deselectAllBtn.addEventListener('click', () => {
    checkboxes.forEach(cb => cb.checked = false);
});

//when get earning release dates is pressed
fetchBtn.addEventListener('click', async () => {
    const selectedTickers = Array.from(checkboxes)
        .filter(cb => cb.checked)
        .map(cb => cb.value);

    if (selectedTickers.length === 0) {
        alert('Please select at least one ticker.');
        return;
    }

    try {
        document.querySelector('.loader').style.display = "block";
        document.querySelector('#earningsTable').style.display = "none";
        const response = await fetch('/api/earnings-release-dates', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ tickers: selectedTickers })
        });

        if (!response.ok) {
            throw new Error(`API error: ${response.status} ${response.statusText}`);
        }

        const data = await response.json();
        populateTable(data);
        document.querySelector('.loader').style.display = "none";
    } catch (error) {
        console.error('Fetch error:', error);
        document.querySelector('.loader').style.display = "none";
    }
});


// populates the table given the json data
function populateTable(data) {
    const tableBody = document.querySelector('#earningsTable tbody');
    // Clear previous rows
    tableBody.innerHTML = '';

    // Populate table
    data.forEach(item => {
        const row = document.createElement('tr');

        const tickerCell = document.createElement('td');
        tickerCell.textContent = item.ticker;

        const dateCell = document.createElement('td');
        dateCell.textContent = item.earnings_date;

        row.appendChild(tickerCell);
        row.appendChild(dateCell);

        tableBody.appendChild(row);
    });
    document.querySelector('#earningsTable').style.display = 'block';
}

//sort order for table
const currentSort = {
    column: null,
    ascending: true
};

//function that sorts talbe
function sortTable(column) {
    const table = document.querySelector('#earningsTable');
    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));

    // Determine sort direction
    if (currentSort.column === column) {
        currentSort.ascending = !currentSort.ascending;
    } else {
        currentSort.column = column;
        currentSort.ascending = true;
    }

    // Determine column index
    const columnIndex = column === 'ticker' ? 0 : 1;

    // Sort rows
    rows.sort((a, b) => {
        const aText = a.children[columnIndex].textContent.trim();
        const bText = b.children[columnIndex].textContent.trim();

        let aValue = aText;
        let bValue = bText;

        // Parse date if sorting by date
        if (column === 'earnings_date') {
            aValue = new Date(aText);
            bValue = new Date(bText);
        }

        return (aValue > bValue ? 1 : -1) * (currentSort.ascending ? 1 : -1);
    });

    // Re-append sorted rows
    rows.forEach(row => tbody.appendChild(row));
}

// Attach event listeners
document.addEventListener('DOMContentLoaded', () => {
    const headers = document.querySelectorAll('#earningsTable th');
    headers[0].addEventListener('click', () => sortTable('ticker'));
    headers[1].addEventListener('click', () => sortTable('earnings_date'));
});

