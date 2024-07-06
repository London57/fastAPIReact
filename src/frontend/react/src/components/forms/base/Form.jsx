
function onsubmit(e) {
    console.log(e.target)
}


export default function Form({fields}) {
    let formFields
    if(fields.length > 1) {
        formFields = Object.values(fields).map((field, index) => (
            <div key={index}>
                <label htmlFor={field} key={index}> {field} </label>
                <input type="text" id={field} key={index} style={{marginBottom: '2em', marginLeft: '2px'}} />
            </div>))
    } else {
        formFields = 
        <div>
            <label htmlFor={fields[0]}> {fields[0]} </label>
            <input type="text" id={fields[0]} style={{marginBottom: '2em', marginTop: '1.3em', marginLeft: '2px'}} />
        </div>
    }

    return (
        <div>
            <form>
                {formFields}
            </form>
            <button type="submit" onSubmit={onsubmit}>submit</button>
        </div>
    )
}