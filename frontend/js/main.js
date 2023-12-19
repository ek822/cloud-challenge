window.addEventListener('DOMContentLoaded', (event) =>{
    getVisitCount(); //calls the function event below
})

const localApiUrl = ''; //TO DO add the URL here

const getVisitCount = () => {
    let count = 30;
    fetch(productionApiUrl).then(response => {
        return response.json()
    }).then(response =>{
        console.log("Website called function API.");
        count =  response.count;
        document.getElementById("counter").innerText = count;
    }).catch(function(error){
        console.log(error);
    });
    return count;
}