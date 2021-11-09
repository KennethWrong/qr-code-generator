<script>
import { select_multiple_value } from "svelte/internal";

  let name = ''
  let json = ''
  let result = null
  let image = ''
  let fetchImgName = ''
  let scanImageURL = ''

  const send_obj_to_qr = async () => {
    const res = await fetch('http://localhost:5000/generate_qr', {
      method: 'POST',
      headers:{
        'Accept':'application/json',
        'Content-Type':'application/json'
      },
      body: JSON.stringify({
        name,
      })
    })
    const response = await res.json()
    console.log(response)
    image = response['image']
  }

  // const scanQRcode = async() => {
  //   const res = await fetch('http://localhost:5000/scan/qr_code',{
  //     method: 'GET'
  //   })
  //   const response = await res.json()
  //   console.log(res)
  // }

  const searchQRcode = async() => {
    let url = 'http://localhost:5000/get_qr_codes/' + fetchImgName+'.png'
    const res = await fetch(url, {
      method: 'GET',
    })
    scanImageURL = url
  }
  
</script>

<h1>Return as QR</h1>
<form>
  <input type="text" bind:value={name} placeholder="Enter your name">
  <button type="button" on:click={send_obj_to_qr}>Generate QR Code</button>
</form>

<img src={image}>
<h1 style='scan'>Scan QR Code</h1>
<form>
  <input type="text"  class="search" bind:value={fetchImgName} placeholder="Look up QR-code">
  <button type="button" on:click={searchQRcode}>Search for QRCode</button>
</form>
<img src={scanImageURL}>

<style>
  .scan{
    margin-top: 20px;
  }

  button:hover{
    background-color: rgb(150, 226, 150);
    cursor: pointer;
  }

</style>

