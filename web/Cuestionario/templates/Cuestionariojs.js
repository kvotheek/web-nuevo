const url = window.location.href  // Sirve para conocer la url

$.ajax({
    type: 'GET',
    url: `${url}casos`,     // referencia a un url que va cambiando con el slash casos y que se encuentra en urls.py
    success: function(response){
        const data = response.data
        data.forEach(el => {
            for (const [question, answers] of Object.entries(el)){
                quizBox.innerHTML += `
                    <hr>
                    <div class="mb-2">
                        <b>${question}</b>
                    </div>
                `
                answers.forEach(answer=>{
                    quizBox.innerHTML += `
                        <div>
                            <input type="radio" class="ans" id="${question}-${answer}" name="${question}" value="${answer}">
                            <label for="${question}">${answer}</label>
                        </div>
                    `
                })
            }
        });
        activateTimer(response.time)
        
    },
    error: function(error){
        console.log(error)
    }
})