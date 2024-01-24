const AVERAGE_SPEED = 20; // Average speed
const EARTH_RADIUS = 6371; // Earth Radius

// Creating graph of nodes to create as given in problem statement
class Graph {
  constructor() {
    this.nodes = {};
  }

  addNode(name, coordinates) {
    this.nodes[name] = {
      coordinates,
      neighbours: []
    }
  }

  addEdge(node1, node2) {
    if (this.nodes[node1].neighbors.includes(node2)) {
      this.nodes[node1].neighbors.push(node2);
      this.nodes[node2].neighbors.push(node1);
    }
  }
}

// Conversion of angle from degree to radium
function convertToRadian(degree) {
  return degree * Math.PI / 180;
}

/**
 * Calculate time taken to travel between point A and B
 * Initially, distance is calculated using haversine formula between A and B
 * provide time taken to travel for calculated distance
 * @param {Number} latA Latitude of location point A
 * @param {Number} latB Latitude of location point B
 * @param {Number} longA Longitude of location point A
 * @param {Number} longB Longitude of location point B
 * @returns Time taken to travel between point A to B by using average speed provided
 */
function haversineDistanceTime(latA, latB, longA, longB) {
  const latitude_distance = convertToRadian(latB - latA);
  const longitude_distance = convertToRadian(longB - longA);

  const a = Math.sin(latitude_distance / 2) ** 2 + Math.cos(toRadians(latA)) * Math.cos(toRadians(latB)) * Math.sin(longitude_distance / 2) ** 2;
  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

  const distance = EARTH_RADIUS * c;
  return distance / AVERAGE_SPEED;
}

/**
 * Calculation of total time taken in path for delivering locations
 * @param {Array} route Path which all places are covered in certain order
 * @param {Object} preparationTimes Time taken to prepare food at the restaurant
 * @param {Object} locations Geo-location values of locations
 * @returns Total time taken to travel in given route
 */
function calculateTotalTime(route, preparationTimes, locations) {
  let totalTime = 0;

  for (let i = 0; i < route.length - 1; i++) {
      const location1 = route[i];
      const location2 = route[i + 1];

      if (location1[0] === 'R') {
          totalTime += preparationTimes[location1];
      }

      totalTime += haversineDistanceTime(...locations[location1], ...locations[location2]);
  }

  return totalTime;
}

/**
 * Checks whether Aman visited Restaurant before delivering to customer
 * @param {String} node Point or location
 * @param {Set} visitedNodes whether location is visited previously
 * @returns boolean based on if Aman visited restaurant before delivering to respective Customer
 */
function isCustomerVisit(node, visitedNodes) {
  if (node[0] === 'C') {
    return visitedNodes.has(`R${node[1]}`);
  }
  return false;
}

/**
 * Calculate shortest time to cover all the locations to delivering orders
 * @param {Graph} graph Graph which contains map of location
 * @param {String} current Current point or location when Aman is located at
 * @param {Set} visited All the visited locations by Aman
 * @param {Array} path All location in order of visited
 * @param {Array} paths Stores all paths with visited route and total time taken
 */
function dfs(graph, current, visited, path, paths) {
  visited.add(current);
  path.push(current);

  if (path.length === Object.keys(graph.nodes).length) {
      const totalTime = calculateTotalTime(path, preparationTimes, locations);
      paths.push({ route: path.slice(), totalTime });
  } else {
      for (const neighbor of graph.nodes[current].neighbors) {
          if (!visited.has(neighbor) && isCustomerVisit(neighbor, visited)) {
              dfs(graph, neighbor, new Set(visited), path, paths);
          }
      }
  }
}

// Locations and mapped with Geo-locations
// Needs to replace latitudes and longitudes of locations with values
const locations = {
  'Aman': [aman_latitude, aman_longitude],
  'R1': [r1_latitude, r1_longitude],
  'R2': [r2_latitude, r2_longitude],
  'C1': [c1_latitude, c1_longitude],
  'C2': [c2_latitude, c2_longitude]
};

// Preparation time taken by each restaurant
// Needs to replace times takes values
const preparationTimes = {'R1': pt1, 'R2': pt2};

// Possible path that Aman can reach from current location to next location
const edges = {
  'Aman': ['R1', 'R2'],
  'R1': ['Aman', 'R2', 'C1', 'C2'],
  'R2': ['Aman', 'R1', 'C1', 'C2'],
  'C1': ['R1', 'R2', 'C2'],
  'C2': ['R1', 'R2', 'C1']
}

/**
 * Calculates optimal accordingly with shortest time taken
 * @returns Optimal Route and minimum time taken to travel
 */
function getShortedTime() {
  const graph = new Graph();
  for (const node in locations) {
      graph.addNode(node, locations[node]);
  }

  for (const node in locations) {
    edges[node].forEach(edgeNode => {
      graph.addEdge(node, edgeNode);
    });
  }

  const paths = [], path = [], visitedNodes = new Set();
  dfs(graph, 'Aman', visitedNodes, path, paths);

  const { route: optimalRoute, totalTime: minTotalTime } = paths.reduce((min, current) => current.totalTime < min.totalTime ? current : min, paths[0]);
  return { optimalRoute, minTotalTime }
}

// Starting function
getShortedTime();
