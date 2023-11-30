/* $(document).ready(function () {
    $("button#start").click(function () {
        $("div#container").append('<form action="/action_page.php">\
        <label for="img">Select image:</label>\
        <input type="file" id="img" name="img" accept="image/*">\
        <input type="submit">\
        </form>');
        $(".start-container").hide();
    })
}) */
$(document).ready(function () {
  $("button#start").click(function () {
    $("div#container").append(
      '<p class=upload-noCss><input type="file"  accept="image/*" name="image" id="file" \
        onchange="loadFile(event)" style="display: none;"></p>\
        <p class="upload"><label for="file" style="cursor: pointer;">Upload Image</label></p>\
        <p><img id="output" width="500px " /></p>'
    );
    $(".start-container").hide();
  });
});

$(document).ready(function () {
    $("#cropImage").click(function () {
        console.log("hello");
    $("p.upload").hide();

  });
});

var loadFile = function (event) {
    var image = document.getElementById("output");
    image.src = URL.createObjectURL(event.target.files[0]);
    $(".upload").hide();
    $("div#container").append('<button id="cropImage" onClick ="btn"> Crop Image </button>');
};
