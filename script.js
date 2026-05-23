// ====== Navbar Toggle ======
const navToggle = document.getElementById("navToggle");
const mainNav = document.getElementById("mainNav");
if (navToggle) {
  navToggle.addEventListener("click", () => {
    mainNav.classList.toggle("active");
  });
}

// ====== Auth System ======
function signupUser() {
  const name = document.getElementById("signupName").value;
  const email = document.getElementById("signupEmail").value;
  const pass = document.getElementById("signupPassword").value;
  if (name && email && pass) {
    localStorage.setItem("user", JSON.stringify({ name, email, pass }));
    alert("Signup successful!");
    window.location.href = "index.html";
  } else {
    alert("Please fill all fields");
  }
}

function loginUser() {
  const email = document.getElementById("loginEmail").value;
  const pass = document.getElementById("loginPassword").value;
  const user = JSON.parse(localStorage.getItem("user"));
  if (user && user.email === email && user.pass === pass) {
    alert("Login successful!");
    window.location.href = "home.html";
  } else {
    alert("Invalid credentials!");
  }
}

function logoutUser() {
  alert("Logged out successfully!");
  window.location.href = "index.html";
}

// ====== Profile ======
const profileName = document.getElementById("profileName");
const profileEmail = document.getElementById("profileEmail");
const editBox = document.getElementById("editBox");

if (profileName && profileEmail) {
  const user = JSON.parse(localStorage.getItem("user"));
  if (user) {
    profileName.textContent = user.name;
    profileEmail.textContent = user.email;
  }
}

function enableEdit() {
  editBox.style.display = "block";
}

function saveProfile() {
  const newName = document.getElementById("editName").value;
  const newEmail = document.getElementById("editEmail").value;
  const user = JSON.parse(localStorage.getItem("user"));
  if (newName) user.name = newName;
  if (newEmail) user.email = newEmail;
  localStorage.setItem("user", JSON.stringify(user));
  alert("Profile updated!");
  window.location.reload();
}

// ====== Feedback ======
function submitFeedback() {
  const fb = document.getElementById("feedbackText").value;
  if (fb.trim() === "") return alert("Please write feedback!");
  alert("Thank you for your feedback!");
  document.getElementById("feedbackText").value = "";
}

// ====== Course Redirect ======
function goToCourse(page) {
  window.location.href = page;
}
// ====== Contact Page ======
function contactSubmit() {
  const name = document.getElementById("contactName").value;
  const email = document.getElementById("contactEmail").value;
  const msg = document.getElementById("contactMessage").value;

  if (!name || !email || !msg) {
    alert("Please fill all fields!");
    return;
  }
  alert("Thank you for contacting us, " + name + "!");
  document.getElementById("contactName").value = "";
  document.getElementById("contactEmail").value = "";
  document.getElementById("contactMessage").value = "";
}
