document.getElementById('calculator-form').addEventListener('submit', function (e) {
    e.preventDefault();

    // Get the input values
    const raspPerWeek = parseInt(document.getElementById('raspPerWeek').value);
    const raspCost = parseFloat(document.getElementById('raspCost').value);
    const years = parseInt(document.getElementById('years').value);

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

