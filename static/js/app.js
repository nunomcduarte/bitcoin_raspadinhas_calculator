document.getElementById('calculator-form').addEventListener('submit', function (e) {
    e.preventDefault();

    // Get the input values
    const raspPerWeek = parseInt(document.getElementById('raspPerWeek').value);
    const raspCost = parseFloat(document.getElementById('raspCost').value);
    let years = parseInt(document.getElementById('years').value);

    // Enforce a maximum of 10 years
    if (years > 10) {
        alert("The number of years cannot exceed 10. Please enter a value between 1 and 10.");
        return;
    }

    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            raspPerWeek: raspPerWeek,
            raspCost: raspCost,
            years: years
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = `
            Total money spent on Raspadinhas over ${years} years: €${data.totalSpent.toFixed(2)}
            Total Bitcoin accumulated: ${data.totalBitcoin.toFixed(6)} BTC
            Potential value if invested in Bitcoin: €${data.investmentValue.toFixed(2)}
        `;
    })
    .catch(error => console.error('Error:', error));
});

