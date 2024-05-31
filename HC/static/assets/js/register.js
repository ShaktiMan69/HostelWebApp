const progressBar = document.querySelector('.progress');


function validateForm() {
    var currentPage = document.querySelector('.page.active');
    var inputs = currentPage.querySelectorAll('input[type="text"], input[type="email"], input[type="file"], input[type="number"], select');
    var isValid = true;

    if (!(document.getElementById('email').value.indexOf('@') > -1)) {
        alert('Please enter an valid email.')
        return
    }

    inputs.forEach(function(input) {
        if (input.value.trim() === '') {
            isValid = false;
            input.classList.add('is-invalid');
        } else {
            input.classList.remove('is-invalid');
        }
    });

    currentPage = currentPage.getAttribute('pageno');
    if (currentPage === '0') {
        var selectors = {'#parent_phone': 10, '#phone': 10}
        var mssg = 'Enter 10 Digit Mobile Numbers Please...';
    };
    if (currentPage === '1'){
        var selectors = {'#pr_number': 9}
        var mssg = 'Enter 9 Digit PR Number Please...';
    };

    for (var key in selectors) {
        if (selectors.hasOwnProperty(key)) {
          if ($(key).val().length !== selectors[key]) {
              alert(mssg);
              return
          }
        }
    };

    return isValid;
}

function fillReview() {
    // Get form data
        var reviewFields = ['name', 'address', 'phone', 'email', 'parent_name', 'parent_phone', 'year', 'semester', 'pr_number', 'department'];

        for (var i = 0; i < reviewFields.length; i++) {
            var field = reviewFields[i];
            var element = document.getElementById(field);
            var reviewElement = document.getElementById('review' + field.charAt(0).toUpperCase() + field.slice(1));
        
            reviewElement.innerHTML = element.value;
        }
  }


function nextPage() {
    if (validateForm()) {
        var currentPage = document.querySelector('.page.active');
        var nextPage = currentPage.nextElementSibling;
        currentPage.classList.remove('active');
        nextPage.classList.add('active');

        
        const photoInput = document.getElementById('photo');
        const photoPreview = document.getElementById('photo-preview');
      
        photoInput.addEventListener('change', function(event) {
          const file = event.target.files[0];
          const reader = new FileReader();
      
          reader.onload = function(event) {
            const img = document.createElement('img');
            img.src = event.target.result;
            photoPreview.innerHTML = ''; // Clear any previous preview
            photoPreview.appendChild(img);
          }
      
          reader.readAsDataURL(file);
        });
    }
    fillReview()
    updateProgressBar();
}
function prevPage() {
  var currentPage = document.querySelector('.page.active');
  var prevPage = currentPage.previousElementSibling;
  currentPage.classList.remove('active');
  prevPage.classList.add('active');
  updateProgressBar();
}

function submitForm() {
  var form = document.getElementById('registrationForm');
  form.submit();
}

function updateProgressBar() {
    const totalPages = document.querySelectorAll('.page').length;
    const currentPage = document.querySelector('.page.active').getAttribute('pageno');
    const progress = ((currentPage) / (totalPages)) * 100;
    progressBar.style.width = progress + '%';
  }

function getSemester() {
    var sem = document.getElementById("year").value;
    if (sem == "FE") {
        var items = ["1", "2"];
    }
    if (sem == "SE") {
        var items = ["3", "4"];
    }
    if (sem == "TE") {
        var items = ["5", "6"];
    }
    if (sem == "BE") {
        var items = ["7", "8"];
    }

    var str = ""
    for (var item of items) {
    str += "<option>" + item + "</option>"
    }
    document.getElementById("semester").innerHTML = str;
}
document.getElementById("year").addEventListener("click", getSemester)
  
