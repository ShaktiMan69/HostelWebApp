const progressBar = document.querySelector('.progress');


function validateForm() {
    var currentPage = document.querySelector('.page.active');
    var inputs = currentPage.querySelectorAll('input[type="text"], input[type="email"], input[type="file"]');
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
