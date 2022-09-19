//types
const GET_USER_BOOKSHELVES = '/bookshelves/user'
const ADD_USER_BOOKSHELF = '/bookshelves/user/add'
const DELETE_USER_BOOKSHELF = '/bookshelves/user/delete'

//actions

const loadBookshelves = (bookshelves) => {
    return {
        type: GET_USER_BOOKSHELVES,
        payload: bookshelves
    }
}

const addUserBookshelf = (bookshelf) => {
    return {
        type: ADD_USER_BOOKSHELF,
        payload: bookshelf
    }
}

const deleteUserBookshelf = (id) => {
    return {
        type: DELETE_USER_BOOKSHELF,
        payload: id
    }
}

//THUNKS

export const getUserBookshelvesThunk = () => async (dispatch) => {
    const response = await fetch('/api/bookshelves/');
    if (response.ok) {
        const data = await response.json();
        dispatch(loadBookshelves(data));
        return JSON.stringify(data);
    }
}

export const addUserBookshelvesThunk = (bookshelf) => async (dispatch) => {

    const response = await fetch('/api/bookshelves/',
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(bookshelf)
        }
    );
    if (response.ok) {
        const data = await response.json();
        dispatch(addUserBookshelf(data));
        return JSON.stringify(data);
    }
}

export const deleteUserBookshelfThunk = (id) => async (dispatch) => {
    const response = await fetch(`/api/bookshelves/${id}`, {
        method: 'DELETE'
    });
    if (response.ok) {
        const data = await response.json();
        dispatch(deleteUserBookshelf(id));
        return JSON.stringify(id);
    }
}

// # //REDUCER
const initialState = { userBookshelves: {} }
const bookshelvesReducer = (state = initialState, action) => {
    let bookshelves
    switch (action.type) {
        case GET_USER_BOOKSHELVES:
            bookshelves = { ...state, userBookshelves: { ...state.userBookshelves } }
            bookshelves.userBookshelves = action.payload
            return bookshelves

        case ADD_USER_BOOKSHELF:
            bookshelves = { ...state, userBookshelves: { ...state.userBookshelves } }
            let newBookshelf = action.payload
            bookshelves.userBookshelves[newBookshelf.id] = newBookshelf
            return bookshelves

        case DELETE_USER_BOOKSHELF:
            bookshelves = { ...state, userBookshelves: { ...state.userBookshelves } }
            let deleteShelfID = action.payload

            delete bookshelves.userBookshelves[deleteShelfID]

            return bookshelves

        default:
            return state
    }
}

export default bookshelvesReducer