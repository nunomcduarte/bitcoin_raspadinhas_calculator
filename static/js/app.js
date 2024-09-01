document.getElementById('calculator-form').addEventListener('submit', function (e) {
    e.preventDefault();
    
    // Get the input values
    const raspPerWeek = parseInt(document.getElementById('raspPerWeek').value);
    const raspCost = parseFloat(document.getElementById('raspCost').value);
    const years = parseInt(document.getElementById('years').value);
    
    // Calculate total money spent
    const totalSpent = raspPerWeek * raspCost * 52 * years;
    
    // For now, let's assume a fixed potential value (you can replace this with real-time data later)
    const potentialValue = totalSpent * 130; // Example multiplier for the potential value
    
    // Display the result
    document.getElementById('result').innerText = `
        Total money spent on Raspadinhas over ${years} years: €${totalSpent.toFixed(2)}
        Potential value if invested in Bitcoin: €${potentialValue.toFixed(2)}
    `;
});
