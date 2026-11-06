
function mytest(){
   
    console.log('inside mytest() function');
    for (i of username){
        console.log(i[0])
    }

}

mytest();
function display_hello_btn(){
    alert('Hello :)' );
    }

function update_user_name_btn(){
    //get the value from the user input
    let user_name_input = document.getElementById('user_name').value;
    //update the span tag with the user input
    document.getElementById('user_name_place_holder').innerHTML = user_name_input;
    }

function calculate_mean(){
    //Get the user data  
    let data_from_user = document.getElementById('user_dataset_1').value;
    //split string data_from_user to list
    let data_in_list = data_from_user.split(',')
    //set up our variables
    let total = 0
    let num_items = 0
    //iterate through the list to get the total
    for (let temp of data_in_list){
    //input is text so we need to cast to float
    total = total + parseFloat(temp);
    } 
    //get the number of items in the list
    num_items = data_in_list.length;
    //calculate the average
    let average = total/num_items
    return average
    }

function calculate_median(){
    let data_from_user = document.getElementById("user_dataset_1").value;

    let data_in_list = data_from_user.split(',')

    let data_length = data_in_list.length
    let middle_value = data_in_list[Math.floor(data_length/2)]
    return middle_value
}

function calculate_mode(){
    let data_from_user = document.getElementById("user_dataset_1").value;
    let data_in_list = data_from_user.split(',')


    let max_count = 0
    let mode = data_in_list[0]
    let checked_values = []

    for (let i of data_in_list){
        if (!checked_values.includes(i));{
            let current_count = 0
            for (let j of data_from_user){
                if (i==j){
                    current_count += 1
                }
            }

            if (current_count > max_count){
                mode = i
                max_count = current_count
            }
        }
    }

    return mode
}

function calculate_range(){
    let data_from_user = document.getElementById("user_dataset_1").value;
    let data_in_list = data_from_user.split(',')
    
    data_in_list = data_in_list.sort()
    let range = 0

    if (data_in_list.length != 1){
        range = data_in_list[data_in_list.length -1] - data_in_list[0]
    }
    return range
}
function calculate_btn(){
    document.getElementById('user_dataset_mean_placeholder').innerHTML = 
    calculate_mean();
    document.getElementById('user_dataset_median_placeholder').innerHTML = 
    calculate_median();
    document.getElementById('user_dataset_mode_placeholder').innerHTML = 
    calculate_mode();
    document.getElementById('user_dataset_range_placeholder').innerHTML = 
    calculate_range();
    }