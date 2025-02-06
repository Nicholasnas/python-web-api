

function emite_alerta_python(){
    alert('python rockes!!');
}
function emite_alerta_django(){
    alert('django alert!!');
}

logo = document.getElementsByTagName('img')[0]
logo_django = document.getElementsByTagName('img')[1]

// Quando houver um clique emite um alerta
logo.onclick = emite_alerta_python;
logo_django.onclick = emite_alerta_django;

