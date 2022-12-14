

// Rating star javascript
const allStar = document.querySelectorAll('.star');
let current_star_level = document.querySelectorAll('.star_rating');

allStar.forEach((star, i) => {
        star.onclick= function() {
            // let current_star_rating = i+1;
            let current_star_level = i + 1;
            // current_star_rating
            allStar.forEach((star, j) => {
                if (current_star_level >= j+ 1){
                    star.innerHTML = '&#9733';
                }else{
                    star.innerHTML = '&#9734';
                }
            })
        }
})