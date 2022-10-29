const usernameField = document.querySelector("#usernameField");
const emailField = document.querySelector("#emailField");
const feedbackArea = document.querySelector(".invalid-feedback");
const emailfeedbackArea = document.querySelector("#emailinvalid");
const showpassword=document.querySelector(".showpassword");
const submitBtn=document.querySelector(".submit-btn");
const confirmpasswordField = document.querySelector("#conpasswordField");
const passfeedback=document.querySelector(".passfeedback");

const handleToggleInput = (e) => {
    if (e.target.classList.contains("showpassword")) {
        if (showpassword.textContent === "SHOW") {
            showpassword.textContent = "HIDE";
            passwordField.setAttribute("type", "text");
        } else {
            showpassword.textContent = "SHOW";
            passwordField.setAttribute("type", "password");
        }
    }
};

showpassword.addEventListener("click",handleToggleInput);


emailField.addEventListener("keyup", (e) => {
  const emailVal = e.target.value;
  if (emailVal.length > 0) {
    emailfeedbackArea.style.display = "block";
  } else {
    emailfeedbackArea.style.display = "none";
  }
  if (emailVal.length > 0) {
    fetch("/authentication/validate-email/", {
      body: JSON.stringify({ email: emailVal }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        if (data.email_error) {
          emailField.classList.add("is-invalid");
          emailfeedbackArea.innerHTML = `<p>${data.email_error}</p>`;
          emailfeedbackArea.style.display = "block";
          submitBtn.setAttribute("disabled", "disabled");
        }
        if (data.email_valid) {
          emailField.classList.remove("is-invalid");
          emailField.classList.add("is-valid");
          emailfeedbackArea.style.display = "none";
          if(confirmpasswordField==passwordField && data.username_valid && data.email_valid){
            submitBtn.removeAttribute("disabled");
          }
        }
      });
  }
});

confirmpasswordField.addEventListener("keyup", (e) => {
  const confirmpasswordVal = e.target.value;

  const passwordVal = passwordField.value;
  if(confirmpasswordVal.length>0){
    if (confirmpasswordVal !== passwordVal) {
      confirmpasswordField.classList.add("is-invalid");
      passfeedback.innerHTML = `<p>Passwords do not match</p>`;
      passfeedback.style.display = "block";
      submitBtn.setAttribute("disabled", "disabled");
    } else {
      confirmpasswordField.classList.remove("is-invalid");
      confirmpasswordField.classList.add("is-valid");
      passfeedback.style.display = "none";
      if(confirmpasswordField==passwordField && data.username_valid && data.email_valid){
        submitBtn.removeAttribute("disabled");
      }
    }
  }
});

usernameField.addEventListener("keyup", (e) => {
  const usernameVal = e.target.value;

  if (usernameVal.length > 0) {
    console.log("code is working")

    fetch("/authentication/validate-username/", {
      body: JSON.stringify({ username: usernameVal }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        console.log("data", data);
        if (data.username_error) {
          usernameField.classList.add("is-invalid");
          feedbackArea.style.display = "block";
          feedbackArea.innerHTML = `<p>${data.username_error}</p>`;
          submitBtn.setAttribute("disabled", "disabled");
        }
        if (data.username_valid) {
          usernameField.classList.remove("is-invalid");
          usernameField.classList.add("is-valid");
          feedbackArea.style.display = "none";
          if(confirmpasswordField==passwordField && data.username_valid && data.email_valid){
            submitBtn.removeAttribute("disabled");
          } 
        }
      });
  }
});
