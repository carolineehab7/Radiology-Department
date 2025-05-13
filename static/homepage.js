document.getElementById('searchButton').addEventListener('click', function() {
    const searchTerm = document.getElementById('searchInput').value;
    const resultsDiv = document.getElementById('results');
    
    if (searchTerm.trim() === '') {
        resultsDiv.innerHTML = '<p>Please enter a search term</p>';
    } else {
        resultsDiv.innerHTML = `<p>You searched for: <strong>${searchTerm}</strong></p>`;
        // Here you would typically make an API call or search through local data
    }
});

// Optional: Add search on Enter key
document.getElementById('searchInput').addEventListener('keyup', function(event) {
    if (event.key === 'Enter') {
        document.getElementById('searchButton').click();
    }
});
// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}
