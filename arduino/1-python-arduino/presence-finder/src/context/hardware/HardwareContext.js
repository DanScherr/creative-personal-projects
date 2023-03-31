import { createContext, /* useState */ useReducer } from "react";
import hardwareReducer from "./HardwareReducer";


const HardwareContext = createContext()
/* const PRESENCE_URL = process.env.REACT_APP_PRESENCE_API_URl + '/api/sensors' */

export const PresenceProvider = ({children}) => {

    /** Reducer */
    const initialState = {
        sensors: [],
        loading: false,
    }
    const [state, dispatch] = useReducer(hardwareReducer, initialState)

    /** Functions */
    const fetchSensors = async () => {
        setLoading(true)
        const response = await fetch('/sensors', {mode: 'no-cors'})
        const data = await response.json()
        dispatch({ //updates the state for the Reducer
            type: 'GET_SENSORS',
            payload: data,
        })
    }

    const setLoading = ( state ) => dispatch({
        type: 'SET_LOADING',
        payload: state
    })

    /** Provider */
    return <HardwareContext.Provider
            value = {{
                sensors: state.sensors,
                loading: state.loading,
                fetchSensors,
            }}
        >
        {children}
    </HardwareContext.Provider>
}

export default HardwareContext