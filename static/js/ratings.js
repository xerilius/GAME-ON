
const starRatings = document.getElementById("star-ratings-grp");
starRatings.addEventListener('click', rateGame);

function rateGame(evt) {
    // console.log(evt.target)
    const starLabel = evt.target;
    console.log(starLabel)
    const ratingValue = document.querySelector('input[name=rating]:checked').value;
    console.log(ratingValue)

    const slug = window.location.pathname.split('/').pop()
    const data = {'star': ratingValue}
    $.post(`/games/${slug}/rating`, data, function()  {
        console.log(".........")
    });
}
