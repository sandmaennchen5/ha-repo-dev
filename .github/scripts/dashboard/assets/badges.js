document.addEventListener("DOMContentLoaded", async ()=>{
 const r = await fetch(BASE_URL + "/data/badges.json");
 const badges = await r.json();
 const tbody = document.querySelector("#badgesTable tbody");
 const search = document.getElementById("badgeSearch");
 function render(items){
   tbody.innerHTML="";
   items.forEach(b=>{
      const tr=document.createElement("tr");
      tr.innerHTML=`<td>${b.app_name||b.app}</td><td>${b.label}</td><td>${b.value||""}</td><td>${b.status||"OK"}</td>`;
      tbody.appendChild(tr);
   });
 }
 render(badges);
 search?.addEventListener("input", ()=>{
   const q=search.value.toLowerCase();
   render(badges.filter(b=>JSON.stringify(b).toLowerCase().includes(q)));
 });
});
