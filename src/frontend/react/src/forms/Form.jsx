
export default function Form({fields}) {
    const formFields = Object.values(fields).map((field, index) => (
        <div key={index}>
            <div>
                <label htmlFor={field} key={index}> {field} </label>
            </div>
            <input type="text" htmlFor={field} key={index} style={{marginBottom: '1em'}} />
        </div>
    ))

    return (
        <div>
            <form>
                {formFields}
            </form>
            <button type="submit">submit</button>
        </div>
    )
}