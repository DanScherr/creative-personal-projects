const chartsReducer = ( state, action ) => {
    switch (action.type) {

        case 'GET_PRESENCES':
            return {
                ...state,
                presences: action.payload,
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

export default chartsReducer