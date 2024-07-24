import axios from "axios"

import './Form.css'
import { useState } from "react"

export default function Form({fields, url_to_send_form, classname, postThen, postCatch}) {
    let formFields
    if (fields.length > 1) {
        formFields = Object.values(fields).map((field, index) => (
            
            <div key={index} className="formElement">
                <input type="text" name={field} style={{marginBottom: '2em', marginLeft: '2px'}}  placeholder={field} />
            </div>))
    } else {
        const field = fields[0]
        formFields = 
        <div className="formElement">
            <input type="text" name={field} style={{marginBottom: '2em',
            marginTop: '5px', marginLeft: '2px'}} placeholder={field}/>
        </div>
    }
    let [errors, SetErrors] = useState([])
    
    let dict = {}
    function onSubmit(e) {
        e.preventDefault()
        SetErrors([])
        let formdata = new FormData(e.target)
        for(let [d, s] of formdata.entries()) {
            dict[d] = s
        }
        axios.post(url_to_send_form, dict)
        .then((res) => {
            if(postThen) {
                postThen(res)
            }
        })
        .catch((r) => {
            let errorsList = []
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
        <form onSubmit={onSubmit} className={`form ${classname}`}>
            {formFields}
            {errors && <p className="errorList">{errors}</p>}
        <button className="buttonSubmit" type="submit">submit</button>
        </form>
    </div>

   
    return form
}