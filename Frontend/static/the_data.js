const statesSelect = document.getElementById("statesSelect");
const statesForm = document.getElementById("statesForm")

statesSelect.addEventListener("change", () => {
  statesForm.submit() 
  console.log("event listener entered")
})