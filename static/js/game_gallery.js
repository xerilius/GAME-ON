const ssArtworks = {{ ss_artworks | tojson }};
document.write(`<div id="carousel" class="carousel slide" data-ride="carousel">`);
document.write(`<div class="carousel-inner">`);

document.write(`<div class="carousel-item active">`);
document.write(`<img class="carousel-slides w-100" src="${ssArtworks.slice(0,1)}">`);
document.write(`</div>`);

for (const img_url of ssArtworks.slice(1)) {
	document.write(`<div class="carousel-item">`);
	document.write(`<img class="carousel-slides w-100" src="${img_url}">`);
	document.write(`</div>`);
	}
document.write(`</div>`)
document.write(`</div>`)
