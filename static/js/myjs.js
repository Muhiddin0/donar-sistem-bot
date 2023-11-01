

let add_wraper_html = document.querySelector('.new-btn-wraper')
const add_wraper = () => {
    add_wraper_html.classList.toggle('active')
}

let btns_wraper_html = document.querySelector('.buttons')
const add_save = () => {

    let btn_name = add_wraper_html.querySelector(`input[placeholder='name']`)
    let btn_url = add_wraper_html.querySelector(`input[placeholder='url']`)
    let btn_html = `
        <div class="bot-btn" id="bot-btn">
            <a href='${btn_url.value}'>${btn_name.value}</a>
            <span onclick='edit_wraper()'><img src="/static/img/icon/pencil.png" alt=""></span>
        </div>
    `

    btns_wraper_html.innerHTML += btn_html
    let old_items =  localStorage.getItem('btns-json')
    if (old_items == null){
        localStorage.setItem('btns-json', btn_html)
    } else {
        localStorage.setItem('btns-json', btn_html + old_items)
    }
    console.log(localStorage.getItem('btns-json'))

    btn_name.value = ''
    btn_url.value = ''

}

let edit_wraper_html = document.querySelector('.edit-btn-wraper')
const edit_wraper = () => {
    edit_wraper_html.classList.toggle('active')
     
    let element = event.currentTarget.parentNode
    let btn_name = element.querySelector('a').textContent
    let btn_url = element.querySelector('a').href
    element.classList.add('is-edit')

    let btns = btns_wraper_html.innerHTML
    localStorage.setItem('btns-json', btns)

    edit_wraper_html.querySelector(`input[placeholder='name']`).value = btn_name
    edit_wraper_html.querySelector(`input[placeholder='url']`).value = btn_url

    // document.querySelector('.buttons')
    // edit_wraper_html.querySelector()
}

const update_btn = () => {
    edit_wraper_html.classList.remove('active')

    let btn_name = edit_wraper_html.querySelector(`input[placeholder='name']`)
    let btn_url = edit_wraper_html.querySelector(`input[placeholder='url']`)
    let btn_html = `
        <a href='${btn_url.value}'>${btn_name.value}</a>
        <span onclick='edit_wraper()'><img src="/static/img/icon/pencil.png" alt=""></span>
    `
    let edit_btn = document.querySelector('.is-edit')

    edit_btn.innerHTML = btn_html
    edit_btn.classList.remove('active')

    let btns_wraper_html = document.querySelector('.buttons')
    localStorage.setItem('btns-json', btns_wraper_html.innerHTML)
}
const delete_btn = () => {
    let edit_btn = document.querySelector('.is-edit')
    edit_btn.remove()
    let btns_wraper_html = document.querySelector('.buttons')
    localStorage.setItem('btns-json', btns_wraper_html.innerHTML)
    let edit_wraper_html = document.querySelector('.edit-btn-wraper')
    edit_wraper_html.classList.remove('active')
}

function getCookie(name) {
    var cookieName = name + "=";
    var cookieArray = document.cookie.split(';');
    
    for(var i = 0; i < cookieArray.length; i++) {
        var cookie = cookieArray[i].trim();
        
        if (cookie.indexOf(cookieName) === 0) {
            return cookie.substring(cookieName.length, cookie.length);
        }
    }
    
    return null; // if the cookie is not found
}

const send_message = () => {
    event.preventDefault()

    // Form date
    let formDate = new FormData()

    // Keyboards
    let btns = []
    let btns_wraper_html = document.querySelectorAll('.buttons a')
    for (let i = 0; i < btns_wraper_html.length; i++) {
        btns.push({
            'url':btns_wraper_html[i].href,
            'title':btns_wraper_html[i].textContent
        })
    }
    
    formDate.append('buttons', "" + JSON.stringify(btns))

    // content
    let content_input = document.querySelector('#content')
    formDate.append('content', content_input.files[0])

    // content
    let text_input = document.querySelector('#captions')
    formDate.append('text', text_input.value)

    // Fetch
    let r = fetch('http://127.0.0.1:8000/xabar-yuborish',{
        method: "POST",
        credentials: "same-origin",
        headers: {
          "X-CSRFToken": getCookie("csrftoken"),
        },
        body:formDate
    })
    .then(r => {
        if (r.status == 200){
            document.querySelector('.buttons').innerHTML = ''
            localStorage.setItem('btns-json', '')
        }
    })
    .catch(err => err)
}   


let old_btns = localStorage.getItem('btns-json')
if (old_btns)
    btns_wraper_html.innerHTML += old_btns

