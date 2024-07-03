import {Navigate} from "react-router-dom"
import {jwtDecode} from "jwt-decode"
import api from "../api"
import { REFRESH_TOKEN, ACCESS_TOKEN } from "../constants"
import { useState } from "react"

function ProtectedRoute({children}) {
    const [isAuthorized, setIsAuthorized] = useState(null)

    const refreshToken = async () => {

    }

    //Look into access token: Do we have one? Is it expired?
    const auth = async () => {
        const token = localStorage.getItem(ACCESS_TOKEN)
        if(!token) {
            setIsAuthorized(false)
            return
        }
        const decoded = jwtDecode(token)
        const tokenExpiration = decoded.exp
        const now = DATE.now() / 1000 // In seconds

        if(tokenExpiration < now) {
            await refreshToken
        } else {
            setIsAuthorized(true)
        }

    //Until state is not null
    if(isAuthorized === null) {
        return <div>Loading...</div>
    }
    
    //Return wrapped children or navigate to login route (router dom)
    return isAuthorized ? children : <Navigate to="/login" />
}

export default ProtectedRoute