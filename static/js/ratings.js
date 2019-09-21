//returns DOM nodes
const labels = document.getElementsByClassName("star-rating");

function resetLabelColors (labels) {
    for (let label of labels) {
        // label.children = list of label.star-ratings
        console.log(label.children)
        label.children[1].style.color = "white";
        // console.log(label)
    }
}

for (let label of labels) {
    const emoji = label.children[1];
    const inputRadio = label.children[0];
    if (inputRadio.checked) {
        emoji.style.color = "#ffc107";
    }

    emoji.addEventListener('click', function() {
        const emojiValue = emoji.dataset.starValue;
        const slug = window.location.pathname.split('/').pop()
        const data = {'star': emojiValue}
        console.log(slug, data);
        $.post(`/games/${slug}/rating`, data, function()  {
            console.log(".........")
        });
        resetLabelColors(labels);
        emoji.style.color = "#ffc107";

        // if document.querySelector('input[name=rating]:checked') {
        //     emoji.style.color = "yellow";
        // }
    });
}
