//JavaScript version to check empty fields
const error_modal = document.getElementById('error_modal')
document.getElementById('submit_form').addEventListener('submit', function(e){
    const form = document.forms[0];
    const trigger = form.elements.id_time_trigger
	const inputs = [
	              form.elements.item(3),
	              form.elements.item(4),
	              form.elements.item(5),
	              form.elements.item(6),
	             ]
	res_string = inputs[0].value+inputs[1].value+inputs[2].value+inputs[3].value;
	if(res_string==='' || Number(res_string)===0){
	    e.preventDefault();
	    error_modal.style.display = 'block'
		error_modal.children[0].children[0].children[1].innerText='Create Task --- You must fill out at least one field ';
	 }else if (!trigger.checked){
	    sch_string = inputs[0].value+inputs[1].value
	    if (sch_string==='' || Number(res_string)===0){
	        e.preventDefault();
	        error_modal.style.display = 'block'
		    error_modal.children[0].children[0].children[1].innerText='Create Task --- If you want to schedule a task, please click on checkbox ';
	    }
	 }

})
document.getElementById('error_close_button').addEventListener('click', function(e){
    error_modal.style.display='none'
})