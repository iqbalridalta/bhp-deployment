function getCredValue() {
  var uich = document.getElementsByName("uich");
  for(var i in uich) {
    if(uich[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getDepValue() {
  var uidep = document.getElementsByName("uidep");
  for(var i in uidep) {
    if(uidep[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getEduValue() {
  var uiedu = document.getElementsByName("uiedu");
  for(var i in uiedu) {
    if(uiedu[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getGenValue() {
  var uigend = document.getElementsByName("uigend");
  for(var i in uigend) {
    if(uigend[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getSelfempValue() {
  var uisemp = document.getElementsByName("uisemp");
  for(var i in uisemp) {
    if(uisemp[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getPropValue() {
  var uiprop = document.getElementsByName("uiprop");
  for(var i in uiprop) {
    if(uiprop[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getMarValue() {
  var uimar = document.getElementsByName("uimar");
  for(var i in uimar) {
    if(uimar[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function onClickedEstimateLoan() {
  console.log("Estimate loan button clicked");
  var gend = getGenValue();
  var dependent = getDepValue();
  var edu = getEduValue();
  var self_emp = getSelfempValue();
  var prop_area = getPropValue();
  var marry = getMarValue();
  var income = document.getElementById("uiApInc");
  var com_income = document.getElementById("uiCoapInc");
  var loan_am = document.getElementById("uiLoA");
  var loan_term = document.getElementById("uiLoAT");
  var credit_hist = getCredValue();
  var estLoan = document.getElementById("uiEstimatedLoan");
  
  var url = "https://loan-data-heroku.herokuapp.com/predict_loan";

  $.post(url, {
      gend : gend,
      dependent : dependent,
      edu : edu,
      self_emp : self_emp,
      prop_area : prop_area,
      marry : marry,
      income : parseFloat(income.value),
      com_income : parseFloat(com_income.value),
      loan_am : parseFloat(loan_am.value),
      loan_term : parseFloat(loan_term.value),
      credit_hist : credit_hist
      
  },function(data, status) {
      console.log(data.loan_prediction);
      estLoan.innerHTML = "<h2>" + data.loan_prediction.toString() + "</h2>";
      console.log(status);
  });
}

function onPageLoad() {
  console.log( "document loaded" );
}

window.onload = onPageLoad;
