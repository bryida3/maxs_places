const allH3s = document.querySelectorAll('.listing');

// Loop through and remove each one
allH3s.forEach(h3 => h3.remove());

function truncateDescription(element) {
    var imgHeight = document.querySelectorAll('.ListingImage')[0].clientHeight;
    console.log(imgHeight)
    document.querySelectorAll('.listing').remove;
    var textContent = 'innerText';
    var parts = element.innerText.split(' ');
    
    while (element.clientHeight > imgHeight) {
        element.style.WebkitLineClamp = element.style.WebkitLineClamp - 1
    }
}

var elements = document.querySelectorAll("div.ListingText");
elements.forEach(element => console.log(element));
    //truncateDescription(element, 5)
    


