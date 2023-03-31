import { createContext, useReducer } from "react";
import chartsReducer from "./ChartsReducer";


const ChartsContext = createContext()


export const ChartProvider = ({children}) => {

    /** Reducer */
    const initialState = {
        sensors: [],
        loading: false,
    }
    const [state, dispatch] = useReducer(chartsReducer, initialState)

    /** Functions */
    const fetchPresences = async () => {
        setLoading(true)
        const response = await fetch('/presences', {mode: 'no-cors'})
        const data = await response.json()
        dispatch({ //updates the state for the Reducer
            type: 'GET_PRESENCES',
            payload: data,
        })
    }

    const setLoading = ( state ) => dispatch({
        type: 'SET_LOADING',
        payload: state
    })

    /** Provider */
    return <ChartsContext.Provider
            value = {{
                presences: state.presences,
                loading: state.loading,
                fetchPresences,
            }}
        >
        {children}
    </ChartsContext.Provider>
}

export default ChartsContext