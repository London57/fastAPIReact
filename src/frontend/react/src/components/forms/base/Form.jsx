import axios from "axios"

import '../RegistrationForm/RegistrationForm.css'

export default function Form({fields, url_to_send_form, classname}) {
    let formFields
    if(fields.length > 1) {
        formFields = Object.values(fields).map((field, index) => (
            <div key={index}>
                <label htmlFor={field}> {field} </label>
                <input type="text" name={field} style={{marginBottom: '2em', marginLeft: '2px'}} />
            </div>))
    } else {
        
        const field = fields[0]
        formFields = 
        <div>
            <label htmlFor={field}> {field} </label>
            <input type="text" name={field} style={{marginBottom: '2em', marginTop: '1.3em', marginLeft: '2px'}} />
        </div>
    }

    let dict = {}
    function onSubmit(e) {
        e.preventDefault()
        let formdata = new FormData(e.target)
        for(let [d, s] of formdata.entries()) {
            dict[d] = s
        }
        axios.post(url_to_send_form, dict)
        window.location.reload()
    }

    let form = 
    <div>
        <form onSubmit={onSubmit} className={classname}>
            {formFields}
        <button type="submit">submit</button>
        </form>
    </div>

   
    return (
        form
    )
}