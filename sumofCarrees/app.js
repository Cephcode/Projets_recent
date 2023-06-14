const list=[0,1,2,3,4,5,6,7,8,9,10]
function paires(list){
    let paires_list=[]
    for (const element of list) {
        
        if(element%2==0){
            paires_list.push(element)
            
        }
    }
    return paires_list
}
function carre(list){
    let nbr_carres=[]
    let l=list.map(e=>{
        console.log(e*e)
        return e*e
    })
    return l
}
function sum(list){
    let sum=0;
    list.forEach(element => {
       sum+=element 
    });
    return sum
}
let nbr_paires=paires(list)
let nbr_carres=carre(nbr_paires)
let sum_carres=sum(nbr_carres)
console.log(sum_carres)
console.log(sum_carres)