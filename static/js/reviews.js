
const deleteButtons = document.getElementsByClassName("delete-review");
for (deleteButton of deleteButtons) {
    console.log(deleteButton)
    deleteButton.addEventListener('click', deleteReview);
}

function deleteReview(evt) {
    console.log(evt.target)
    const deleteButton = evt.target;
    const reviewId = deleteButton.dataset.reviewId;
    console.log($, $.post)

    $.post(`/reviews/${reviewId}/delete`, function()  {
        console.log("did this work");
        const removeReview = deleteButton.parentNode
        removeReview.remove();
    });
}
