import React from 'react';
import { StyleSheet, AppRegistry, FlatList, ActivityIndicator, Text, View  } from 'react-native';

export default class FetchExample extends React.Component {

  constructor(props){
    super(props);
    this.state ={ isLoading: true}
  }

  componentDidMount(){
    fetch('http://192.168.1.8:8000/api/product_list/?format=json', {
  method: 'POST',
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    name: 'yourValue',
    price: 'yourOtherValue',
  }),
}).then((response) => response.json())
    .then((responseJson) => {
      return responseJson;
    })
    .catch((error) => {
      console.error(error);
    });

  }


  render(){

    if(this.state.isLoading){
      return(
        <View style={{flex: 1, padding: 20}}>
          <ActivityIndicator/>
        </View>
      )
    }

    return(
      <View style={{flex: 20, paddingTop:20}}>
        <FlatList
          data= componentDidMount();
          renderItem={({item}) =>
          <View>
          <Text style={[styles.bigblue]} > {item.name} </Text>
          <Text style={[styles.bigblue, styles.red]}> R${item.price.toFixed(2)} </Text>
          <Text> {item.description} </Text>
          </View>
        }
          keyExtractor={(item, index) => index}
        />
      </View>
    );
  }
}
const styles = StyleSheet.create({
  bigblue: {
    color: 'blue',
    fontWeight: 'bold',
    fontSize: 30,
  },
  red: {
    color: 'red',
  },
});
