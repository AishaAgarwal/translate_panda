// dashboard - Header dropdown
function myFunction() {
  document.getElementById("myDropdown2").classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn1')) {
    var dropdowns = document.getElementsByClassName("dropdown-content_1");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
} 



// dashboard - Hide the video upload content 
$(document).ready(function(){
  $(".custom-file-upload").click(function(){
    $(".file-upload i").hide();
    $(".file-upload h1").hide();
    $(".file-upload p").hide();
    $(".file-upload a").hide();
    $(".custom-file-upload").hide();
  });
});

// dashboard - Upload video
jQuery(document).ready(function($){
 
    // Click button to activate hidden file input
$('.fileuploader-btn').on('click', function(){
  $('.fileuploader').click();
  });
  
    // Click above calls the open dialog box
    // Once something is selected the change function will run
$('.fileuploader').change(function(){
  
    // Create new FileReader as a variable
var reader = new FileReader();
  
    // Onload Function will run after video has loaded
reader.onload = function(file){
  var fileContent = file.target.result;
  $('.video-list ul').append('<video src="' + fileContent + '" width="420" height="210" controls></video>');
  }
  
  // Get the selected video from Dialog
  reader.readAsDataURL(this.files[0]);
  $(".Upload").show();
  $(".Upload").text("Upload Now");
  });
});



// index -  Modal function
var modal = document.getElementById('id01');

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}


// dashboard - video card dropdown
function myFunction6() {
  document.getElementById("myDropdown").classList.toggle("show");
}

window.onclick = function(event) {
  if (!event.target.matches('.dropbtn6')) {
    var dropdowns = document.getElementsByClassName("dropdown-content6");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}



// video card modal
var modal = document.getElementById('id02');

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "show";
    }
}


// upgrade-modal
var modal = document.getElementById('id03');

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "show";
    }
}

// share-modal
var modal = document.getElementById('id04');

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "show";
    }
}

// Social media share
function myFunction1() {
  window.open("https://www.linkedin.com");
}

function myFunction2() {
  window.open("https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fdevelopers.facebook.com%2Fdocs%2Fplugins%2F&amp;src=sdkpreparse");
}

function myFunction3() {
  window.open("https://web.whatsapp.com/");
}

function myFunction4() {
  window.open("https://www.instagram.com/?url=https%3A%2F%2Fwww.drdrop.co%2F/");
}

function myFunction5() {
  window.open("https://www.youtube.com/");
}



function updateProgressBar() {
//   // Make an AJAX request to get the progress
  $.ajax({
      url: '/get_progress',
      type: 'GET',
      success: function(data) {
          // Update the progress bar value
          document.getElementById('progress').value = data.progress;
      },
      error: function(error) {
          console.error('Error fetching progress:', error);
      }
  });
 }

// Call updateProgressBar function every few seconds
setInterval(updateProgressBar, 3000);
 // Adjust the interval as needed
