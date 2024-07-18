import axios from "axios"

import '../RegistrationForm/RegistrationForm.css'
import { useState } from "react"

export default function Form({fields, url_to_send_form, classname}) {
    let formFields
    if (fields.length > 1) {
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
    let [errors, SetErrors] = useState([])

    let dict = {}
    console.log(formFields)
    function onSubmit(e) {
        e.preventDefault()
        SetErrors([])
        let formdata = new FormData(e.target)
        for(let [d, s] of formdata.entries()) {
            dict[d] = s
        }
        console.log('axios')
        axios.post(url_to_send_form, dict)
        .then((res) => {
            if (res.status === 201) {
                console.log('success')
            }
        })
        .catch((r) => {
            let errorsList = []
            console.log(r)
            console.log('rrrrrrrr', )
            console.log('tt', r.response.data.detail)
            if (r.response.data.detail === 'REGISTER_USER_ALREADY_EXISTS') {
                errorsList.push(<p style={{'color': 'tomato', 'flex': '0 0 auto'}}>this email already exists</p>)
            }

            else if (typeof(r.response.data.detail) === 'string') {
                errorsList.push(<p style={{'color': 'tomato', 'flex': '0 0 auto'}}>{r.response.data.detail}</p>)
            }
            else {
                r.response.data.detail.forEach((element) => {
                    errorsList.push(<p style={{'color': 'tomato', 'flex': '0 0 auto'}}>{element.msg}</p>)
                })
            }
            SetErrors(errorsList)
        })

        // window.location.reload()
    }
    console.log(errors)
    let form = 
    <div>
        <form onSubmit={onSubmit} className={classname}>
            {formFields}
            {errors && errors}
        <button type="submit">submit</button>
        </form>
    </div>

   
    return form
}