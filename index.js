// scroll up button
let topIcon = document.querySelector('.toTop');
let pageTopLocation;
window.addEventListener('scroll',function() {
    pageTopLocation = window.pageYOffset;
    if (pageTopLocation>10) {
        topIcon.style.display = 'block';
    } else{
    topIcon.style.display = "none";
    }
});

// subscribe email section (area)
document.querySelector('.submit-email').addEventListener('mousedown', (e) => {
    e.preventDefault();
    document.querySelector('.subscription').classList.add('done');
  });
