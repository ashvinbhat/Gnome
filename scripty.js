let box2 = document.querySelector(".box-2");
let result = document.querySelector(".result");
let cropped_holder = document.querySelector(".cropped_holder");
let cropped_img = document.querySelector(".cropped_img");
let submit = document.querySelector(".submit")
let reset1 = document.querySelector(".reset1")
let upload = document.querySelector("#upload1");
//const { default: Cropper } = require("cropperjs");
//const cropper = require("cropperjs")

const reader = new FileReader();


upload.addEventListener('change', 
(e)=>{
    console.log(e);
    const reader = new FileReader();
    reader.onload = (e)=>
    {
        if(e.target.result)
        {
            
            let img1 = document.createElement("img");
            img1.src= e.target.result;
            img1.id= "result_img";

            img1.innerHTML ="";
            result.appendChild(img1);

            submit.classList.remove("hide");
            //start cropper
            crop = new Cropper(img1,);
            
        }
        
    }
    reader.readAsDataURL(e.target.files[0]);
});

submit.addEventListener('click',(e)=>
{
    e.preventDefault();
    //let imgsrc = crop.getCroppedCanvas().toDataURL();
    
    var img_itself = document.createElement('img');
    img_itself = crop.getCroppedCanvas();
    
    cropped_holder.appendChild(img_itself);
    result.classList.add("hide");
    cropped_holder.classList.remove("hide");
    reset1.classList.remove("hide");
    submit.classList.add("hide");




    /*console.log(imgsrc);
    cropped_img.src = imgsrc;
    cropped_holder.classList.remove("hide");
    cropped_img.classList.remove("hide");*/

});

reset1.addEventListener('click',(e)=>
{   upload.value="";
    crop.destroy();
    /*cropped_holder.classList.add("hide");
    cropped_img.classList.add("hide");
    reset1.classList.add("hide");
    submit.classList.remove("hide");
    upload.addEventListener('change',upload_image(e));
    submit.addEventListener('click',submit_crop(e));
    */

})



