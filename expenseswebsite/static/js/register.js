const usernameField = document.querySelector("#usernameField");
const emailField = document.querySelector("#emailField");
const feedbackArea = document.querySelector(".invalid-feedback");
const emailfeedbackArea = document.querySelector("#emailinvalid");

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
        }
        if (data.email_valid) {
          emailField.classList.remove("is-invalid");
          emailField.classList.add("is-valid");
          emailfeedbackArea.style.display = "none";
        }
      });
  }
});

usernameField.addEventListener("keyup", (e) => {
  const usernameVal = e.target.value;

  if (usernameVal.length > 0) {
    fetch("/authentication/validate-username/", {
      body: JSON.stringify({ username: usernameVal }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        console.log("data", data);
        if (data.username_error) {
          usernameField.classList.add("is-invalid");
          // console.log("code is working")
          feedbackArea.style.display = "block";
          feedbackArea.innerHTML = `<p>${data.username_error}</p>`;
        }
        if (data.username_valid) {
          usernameField.classList.remove("is-invalid");
          usernameField.classList.add("is-valid");
          feedbackArea.style.display = "none";
        }
      });
  }
});
