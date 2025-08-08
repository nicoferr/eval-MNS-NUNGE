import { useEffect, useState } from "react"

export default function History() {
    const [ cocktails, setCocktails] = useState([])

    useEffect(() => {
        fetch('http://127.0.0.1:5000/cocktails')
        .then((response) => {
            return response.json()
        })
        .then((json) => {
            console.log("REPONSE JSON", json)
            setCocktails(json)
        });
    }, [])

    return (
        <div className="flex flex-col p-4 w-full md:flex-row md:flex-wrap">
            {cocktails.map((cocktail, key) => {
                return (
                    <div key={key} className="my-2 md:mx-2 md:max-w-3/10 p-2 w-md border-1 border-gray-200 hover:shadow text-justify">
                       <span className="text-2xl">{cocktail.name}</span>
                       <div className="my-2">
                            <span className="text-lg underline">Ingrédients</span>
                            <div>{cocktail.ingredients}</div>
                        </div>
                       <div className="my-2">
                            <span className="text-lg underline">Description</span>
                            <div>{cocktail.description}</div>
                        </div>
                       <div className="my-2">
                            <span className="text-lg underline">Musique</span>
                            <div>{cocktail.music}</div>
                        </div>
                    </div>
                    
                )
            })}
        </div>
    )
}