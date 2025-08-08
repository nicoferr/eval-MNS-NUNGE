import { useEffect, useState } from "react";

export default function Form() {
    const [ context, setContext ] = useState("")
    const [ loading, setLoading ] = useState(false)

    function handleSubmit(e) {
        e.preventDefault();
        setLoading(true)

        fetch('http://127.0.0.1:5000/cocktails/new', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ context: context })
        })
        .then((response) => {
            return response.json()
        })
        .then((json) => {
            if(json.message) alert(json.message)
            if(json.error) alert(json.error)
            setLoading(false)
        });
    }

    return (
        <>
            {loading && <p className="p-3 bg-blue-300">Veuillez patienter pendant la génération du cocktail</p>}
            <div className="flex justify-center w-full py-10">
                <form className="flex flex-col items-center p-3 w-100 border-1 border-gray-200 shadow rounded" onSubmit={handleSubmit}>
                    <label className="m-4 w-full" htmlFor="context">Demander un nouveau cocktail :</label>
                    <textarea className="w-full border-1 h-80 p-2" onChange={(e) => setContext(e.target.value)}></textarea>
                    <button className="m-4 bg-blue-400 hover:bg-blue-500 text-white p-2 cursor-pointer">Commander</button>
                </form>
            </div>
        </>
    )
}