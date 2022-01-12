$(document).ready(function () {
  $("#alladmissionTable").DataTable();
});
$(document).ready(function () {
  $("#classnurseryTable").DataTable();
  $("#classlkgTable").DataTable();
  $("#classukgTable").DataTable();
  $("#classoneTable").DataTable();
  $("#classtwoTable").DataTable();
  $("#classthreeTable").DataTable();
  $("#classfourTable").DataTable();
  $("#classfiveTable").DataTable();
  $("#classsixTable").DataTable();
  $("#classsevenTable").DataTable();
  $("#classeightTable").DataTable();
});


$(document).ready(function () {
  $("#sidebarCollapse").on("click", function () {
    $("#sidebar").toggleClass("active");
  });
});

var popoverTriggerList = [].slice.call(
  document.querySelectorAll('[data-bs-toggle="popover"]')
);
var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
  return new bootstrap.Popover(popoverTriggerEl);
});
var popover = new bootstrap.Popover(
  document.querySelector(".example-popover"),
  {
    container: "body",
    trigger: "hover",
  }
);

function ShowHideDiv() {
    var dropdownid = document.getElementById("dropdownid");
    var zero = document.getElementById("zero");
    var nursery = document.getElementById("nursery");
    var lkg = document.getElementById("lkg");
    var ukg = document.getElementById("ukg");
    var one = document.getElementById("one");
    var two = document.getElementById("two");
    var three = document.getElementById("three");
    var four = document.getElementById("four");
    var five = document.getElementById("five");
    var six = document.getElementById("six");
    var seven = document.getElementById("seven");
    var eigth = document.getElementById("eight");
    zero.style.display = dropdownid.value == "zero" ? "flex" : "none";
    nursery.style.display = dropdownid.value == "nursery" ? "block" : "none";
    lkg.style.display = dropdownid.value == "lkg" ? "block" : "none";
    ukg.style.display = dropdownid.value == "ukg" ? "block" : "none";
    one.style.display = dropdownid.value == "one" ? "block" : "none";
    two.style.display = dropdownid.value == "two" ? "block" : "none";
    three.style.display = dropdownid.value == "three" ? "block" : "none";
    four.style.display = dropdownid.value == "four" ? "block" : "none";
    five.style.display = dropdownid.value == "five" ? "block" : "none";
    six.style.display = dropdownid.value == "six" ? "block" : "none";
    seven.style.display = dropdownid.value == "seven" ? "block" : "none";
    eigth.style.display = dropdownid.value == "eight" ? "block" : "none";
}
