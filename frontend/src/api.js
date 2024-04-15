import { API_URL } from './config'

const GetNews = async (nums_of_news) => {
    const response = await fetch(API_URL + '?nums_of_news=' + nums_of_news);
    return await response.json();
}

export {GetNews};