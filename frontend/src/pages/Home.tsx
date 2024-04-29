import { Button } from "@/components/ui/button"
import { useState } from "react"

export default function Home() {
    const [int, setInt] = useState(0)

    const increment = () => {
        setInt(prevInt => prevInt +1)
    }
    return(
        <>
            <h1>Home</h1>
            <p>{int}</p>
            <Button onClick={increment}>Increment</Button>
        </>
    )
}