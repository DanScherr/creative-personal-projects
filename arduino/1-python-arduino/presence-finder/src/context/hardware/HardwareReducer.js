const hardwareReducer = ( state, action ) => {
    switch (action.type) {

        case 'GET_SENSORS':
            return {
                ...state,
                sensors: action.payload,
                loading: false,
            }
        
        case 'SET_LOADING':
            return {
                ...state,
                loading: true,
            }
    
        default:
            return state // if no action, return current state
    }
}

export default hardwareReducer