submitbtn.addEventListener("click", (e) => {
    e.preventDefault();
    const promptTxt = imgprompt.value;
    fetch("/generateimages/" + promptTxt)
        .then(response => response.json())
        .then(data => {
            console.log(data);
            // const images = data.images;
            // const container = document.querySelector(".container");
            // images.forEach(image => {
            //     const img = document.createElement("img");
            //     img.src = image;
            //     container.appendChild(img);
            // })
        })
    })