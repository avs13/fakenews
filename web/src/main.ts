import './style.css'
import './index.css'



const alertFalse = document.querySelector<HTMLDivElement>('#false')!
const alertTrue = document.querySelector<HTMLDivElement>('#true')!
const propabilityMessage = document.querySelector<HTMLDivElement>('#probability')!
  
const detect = document.querySelector<HTMLButtonElement>('#detect')!
const clear = document.querySelector<HTMLButtonElement>('#clear')!
  
const textarea = document.querySelector<HTMLTextAreaElement>('textarea')!
  
const score = document.querySelector<HTMLSpanElement>('#score')!
  
function clearTextArea(){
  textarea.value = ''
}
  
function hiddenMessages() {
  alertFalse.classList.add('hidden')
  alertTrue.classList.add('hidden')
  propabilityMessage.classList.add('hidden')
}
  
clear.addEventListener('click', () => {
  clearTextArea()
  hiddenMessages()
})
  
  
detect.addEventListener("click",async () => {
  if(textarea.value === '') {
    alert('Ingresar noticia')
    return
  }
  
  hiddenMessages()
  const propability = await fetchNewsDetection(textarea.value)
  propabilityMessage.classList.remove('hidden')
  if(propability > 0.5) {
    alertFalse.classList.remove('hidden')
  }
  else {
    alertTrue.classList.remove('hidden')
  }

  score.innerText = (propability * 100).toString() + "%"
})
  
function fetchNewsDetection(news: string) {
  return fetch('http://localhost:8000/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({news})
  })
  .then(res => res.json()).then(data=>parseFloat(data.acurancy))
}