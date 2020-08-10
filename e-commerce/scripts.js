const hearts = document.querySelectorAll('.wishlist')
const number = document.getElementById('wishlistNumber')

hearts.forEach(heart => {
    heart.addEventListener('click', wishlist, {once: true})
})
function wishlist(){
        number.innerText++
        number.style.color = 'red'
}
