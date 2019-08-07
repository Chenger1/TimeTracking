//Set 'category' value
/*var category = document.getElementById('id_categories');
var name = document.getElementById('category').innerText;
for (var i=0;i<category.length;i++){
	if (category.options[i].innerText === name){
		category.options[i].setAttribute('selected', true)
	}
}
*/
const forms = document.forms
document.body.addEventListener('click', (event) => {
  if (event.target.matches('#change_button')) {
    hide_time_in_change_form(event)
  }else if(event.target.matches('#add_task')){
    hide_time_in_add_form(event)
  }
})
function hide_time_in_change_form(event){
    let form = forms[event.target.name]
    let trigger = form.elements.id_time_trigger
    let time_area1 = form.elements.time_spent_hour
    let time_area2 = form.elements.time_spent_minute
    localStorage['time_area1'] = time_area1.value
    localStorage['time_area2'] = time_area2.value
    let close_button = form.elements.namedItem('close_button')
    let submit_button = form.elements.namedItem('submit_button')
    let currently_time = time_area1.parentNode.parentNode.parentNode
    trigger.addEventListener('click', function(e){
    if(trigger.checked==true){
        currently_time.style.display='none'
        time_area1.value = 0
        time_area2.value = 0
    }else{
        currently_time.style.display='flex'
        time_area1.value = localStorage['time_area1']
        time_area2.value = localStorage['time_area2']
         }
    })
    close_button.addEventListener('click', function(e){
        trigger.checked=false
        currently_time.style.display='flex'
        time_area1.value = localStorage['time_area1']
        time_area2.value = localStorage['time_area2']

    })
}
function hide_time_in_add_form(event){
    trigger = document.getElementsByClassName('checkboxinput')[0]
    currently_time = document.getElementsByClassName('currently')[0]
    trigger.addEventListener('click', function(e){
	    if (trigger.checked ===true){
		    currently_time.style.display='none'
	    }else{
		    currently_time.style.display='flex'
            }
    })
}


